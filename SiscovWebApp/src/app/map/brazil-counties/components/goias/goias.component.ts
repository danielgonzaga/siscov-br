import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-goias',
  templateUrl: './goias.component.html',
  styleUrls: ['./goias.component.css']
})
export class GoiasComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}
