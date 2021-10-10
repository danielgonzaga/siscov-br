import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PiauiComponent } from './piaui.component';

describe('PiauiComponent', () => {
  let component: PiauiComponent;
  let fixture: ComponentFixture<PiauiComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PiauiComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PiauiComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
