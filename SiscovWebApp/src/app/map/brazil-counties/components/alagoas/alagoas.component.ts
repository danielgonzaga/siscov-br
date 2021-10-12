import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-alagoas',
  templateUrl: './alagoas.component.html',
  styleUrls: ['./alagoas.component.css']
})
export class AlagoasComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }
}
