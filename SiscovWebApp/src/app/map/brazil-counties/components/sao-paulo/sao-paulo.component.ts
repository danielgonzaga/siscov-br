import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-sao-paulo',
  templateUrl: './sao-paulo.component.html',
  styleUrls: ['./sao-paulo.component.css']
})
export class SaoPauloComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}
